# 代码生成时间: 2025-10-23 22:07:07
import gradio as gr
def purchase_item(item_id, quantity):
    # 模拟数据库中的商品信息
    products = {
        "1": {"name": "Product A", "price": 100},
        "2": {"name": "Product B", "price": 200},
        "3": {"name": "Product C", "price": 300}
    }
    # 检查商品是否存在
    if item_id not in products:
        raise ValueError("Item not found")
    # 计算总价
    total_price = products[item_id]["price"] * quantity
    return {"item_id": item_id, "quantity": quantity, "total_price": total_price}

# 创建Gradio界面
iface = gr.Interface(
    fn=purchase_item,
    inputs=[
        gr.Textbox(label="Item ID"),
        gr.Slider(label="Quantity", minimum=1, maximum=100, step=1)
    ],
    outputs=gr.JSON(),
    title="B2B Purchase System",
    description="A simple B2B purchase system interface using Gradio."
)

# 运行Gradio界面
iface.launch()