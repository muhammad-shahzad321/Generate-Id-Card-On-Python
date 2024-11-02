from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt


from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# Load your uploaded image
image_path = "/content/umar.jpg"
profile_img = Image.open("/content/umar.jpg")
profile_img = profile_img.resize((100, 120))  # Resize to fit on the card

# Set up ID card dimensions and colors
width, height = 600, 350
background_color = (240, 248, 255)   # Light blue background
header_color = (0, 102, 204)         # Dark blue header
text_color = (0, 51, 102)            # Dark text color
info_color = (255, 255, 255)         # White for info section background
signature_color = (34, 139, 34)      # Green for signature section

# Create an empty image with background color
card = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(card)

# Load font (use default font if a custom font isn't available)
try:
    font_title = ImageFont.truetype("arial.ttf", 24)
    font_text = ImageFont.truetype("arial.ttf", 18)
except IOError:
    font_title = ImageFont.load_default()
    font_text = ImageFont.load_default()

# Draw Header
draw.rectangle([(0, 0), (width, 60)], fill=header_color)
draw.text((width // 2 - 70, 15), "ID CARD", fill="white", font=font_title)

# Place the Profile Image on the Card
card.paste(profile_img, (width - 130, 80))  # Position the image on the right

# Information to display on the card
info = {
    "Name": "Muhammad Shahzad",
    "Roll No": "PIAIC245631",
    "Distance Learning": "No",
    "City": "Karachi",
    "Center": "Bahria Auditorium",
    "Campus": "Karsaz",
    "Days / Time": "Sunday - 09:00 AM to 01:00 PM",
    "Batch": "61"
}

# Add Personal Information
y_offset = 80
for key, value in info.items():
    draw.rectangle([(20, y_offset - 5), (width - 150, y_offset + 25)], fill=info_color)
    draw.text((30, y_offset), f"{key}: {value}", fill=text_color, font=font_text)
    y_offset += 30

# Draw Authorized Signature Section
draw.rectangle([(0, height - 50), (width, height)], fill=signature_color)
draw.text((width // 2 - 70, height - 40), "Authorized Signature", fill="white", font=font_text)

# Display the final ID card
plt.imshow(card)
plt.axis("off")
plt.show()

# Set up ID card dimensions and colors
width, height = 600, 350
background_color = (240, 248, 255)   # Light blue background
header_color = (0, 102, 204)         # Dark blue header
text_color = (0, 51, 102)            # Dark text color
info_color = (255, 255, 255)         # White for info section background
signature_color = (34, 139, 34)      # Green for signature section

# Create an empty image with background color
card = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(card)

# Load font (use default font if a custom font isn't available)
try:
    font_title = ImageFont.truetype("arial.ttf", 24)
    font_text = ImageFont.truetype("arial.ttf", 18)
except IOError:
    font_title = ImageFont.load_default()
    font_text = ImageFont.load_default()

# Draw Header
draw.rectangle([(0, 0), (width, 60)], fill=header_color)
draw.text((width // 2 - 70, 15), "ID CARD", fill="white", font=font_title)

# Place the Profile Image on the Card
card.paste(profile_img, (width - 130, 80))  # Position the image on the right

# Information to display on the card
info = {
    "Name": "Muhammad Shahzad",
    "Roll No": "PIAIC245631",
    "Distance Learning": "No",
    "City": "Karachi",
    "Center": "Bahria Auditorium",
    "Campus": "Karsaz",
    "Days / Time": "Sunday - 09:00 AM to 01:00 PM",
    "Batch": "61"
}

# Add Personal Information
y_offset = 80
for key, value in info.items():
    draw.rectangle([(20, y_offset - 5), (width - 150, y_offset + 25)], fill=info_color)
    draw.text((30, y_offset), f"{key}: {value}", fill=text_color, font=font_text)
    y_offset += 30

# Draw Authorized Signature Section
draw.rectangle([(0, height - 50), (width, height)], fill=signature_color)
draw.text((width // 2 - 70, height - 40), "Authorized Signature", fill="white", font=font_text)

# Display the final ID card
plt.imshow(card)
plt.axis("off")
plt.show()