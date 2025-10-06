# 代码生成时间: 2025-10-06 18:46:28
import gradio as gr
import alembic.config
from alembic import command
from alembic.util import sqla
from sqlalchemy import engine_from_config
import logging

# Set up logging configuration
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DatabaseMigrationTool:
    def __init__(self):
        # Initialize the Alembic configuration
        self.config = alembic.config.Config()
        self.config.set_main_option("script_location", "migrations")
        self.config.set_main_option("sqlalchemy.url", "postgresql://user:password@host:port/dbname")
        self.connection = None

    def connect_to_database(self):
        # Establish a connection to the database
        try:
            self.connection = sqla.CaptureConnectionContext(
                engine_from_config(self.config.get_section("postgresql"), prefix="sqlalchemy.").connect()
            )
        except Exception as e:
            logger.error("Failed to connect to the database: ", exc_info=e)
            raise

    def run_migration(self):
        # Run the Alembic migration
        if not self.connection:
            self.connect_to_database()
        try:
            with self.connection.begin() as conn:
                command.upgrade(self.config, "head")
                logger.info("Migration successful")
        except Exception as e:
            logger.error("Migration failed: ", exc_info=e)
            raise

    def rollback_migration(self):
        # Rollback the last Alembic migration
        if not self.connection:
            self.connect_to_database()
        try:
            with self.connection.begin() as conn:
                command.downgrade(self.config, "-1")
                logger.info("Rollback successful")
        except Exception as e:
            logger.error("Rollback failed: ", exc_info=e)
            raise

# Create a Gradio interface for the DatabaseMigrationTool
def main():
    migration_tool = DatabaseMigrationTool()
    with gr.Blocks() as demo:
        gr.Markdown("This is a database migration tool.")
        
        with gr.Row():
            migrate_button = gr.Button("Migrate")
            rollback_button = gr.Button("Rollback")
            
        migrate_button.click(migration_tool.run_migration, inputs=[], outputs=[gr.Textbox(label="Migration Result")])
        rollback_button.click(migration_tool.rollback_migration, inputs=[], outputs=[gr.Textbox(label="Rollback Result")])
        
    demo.launch()

if __name__ == "__main__":
    main()