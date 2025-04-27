from PIL import Image, ImageDraw, ImageFont

# إعداد الصورة
image_size = (800, 400)  # الحجم الكلي للصورة
bg_color = (0, 0, 0)  # خلفية باللون الأسود
font_color = (50, 255, 50)  # لون النص (أخضر نعناع)
name = "Hussein Bakr"  # اسمك في الصورة

# إنشاء صورة جديدة
img = Image.new('RGB', image_size, color=bg_color)
draw = ImageDraw.Draw(img)

# تحديد الخط
font = ImageFont.load_default()  # يمكنك استخدام خط مخصص هنا

# حساب موقع النص بحيث يكون في وسط الصورة
text_width, text_height = draw.textsize(name, font=font)
text_position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)

# رسم النص
draw.text(text_position, name, font=font, fill=font_color)

# حفظ الصورة كـ PNG أو GIF (اختياري)
img.save("snake_image.png")
