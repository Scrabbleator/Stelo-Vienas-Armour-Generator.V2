import streamlit as st

# Set app title
st.title("Stelo Vienas Armor Generator")
st.subheader("Customize your character's armor for ultimate personalization!")

# Sidebar: Armor Customization
st.sidebar.header("Armor Customization")

# Base Layer Options
base_layer = st.sidebar.selectbox(
    "Base Layer (Under Armor)",
    ["None", "Gambeson", "Arming Doublet", "Chainmail Hauberk", "Leather Jerkin"]
)

# Over-Armor Options
over_armor = st.sidebar.multiselect(
    "Over Armor (Outer Layer)",
    ["None", "Hooded Tunic", "Flowing Cape", "Heraldic Surcoat", "Fur-Lined Mantle"]
)

# Armor Material Options (Expanded)
armor_material = st.sidebar.selectbox(
    "Primary Armor Material",
    ["Steel", "Bronze", "Gold", "Blackened Iron", "Mithril", "Adamantine", "Hardened Leather", "Bone"]
)

# Helmet Options
helmet = st.sidebar.selectbox(
    "Helmet",
    ["None", "Great Helm", "Bascinet", "Sallet", "Visored Helm", "Hood with Armor"]
)

# Shoulder Armor Options
shoulder_armor = st.sidebar.selectbox(
    "Shoulder Armor",
    ["None", "Spaulders", "Pauldrons", "Scaled Shoulders", "Winged Pauldrons"]
)

# Engravings & Patterns
engraving_style = st.sidebar.selectbox(
    "Engraving Style",
    ["None", "Floral", "Runes", "Geometric", "Celtic Knots", "Nordic Symbols", "Arcane Glyphs"]
)

# Decorative Options
decorative_features = st.sidebar.multiselect(
    "Additional Decorative Features",
    ["None", "Mythical Creatures", "Battle Scars", "Dragon Scale Etching", "Custom Symbol"]
)

# Color Customization
st.sidebar.header("Color Customizations")
base_layer_color = st.sidebar.color_picker("Base Layer Color (Gambeson, Tunic)", "#B87333")
armor_accent_color = st.sidebar.color_picker("Armor Accent Color", "#FFD700")
cloak_color = st.sidebar.color_picker("Cloak or Cape Color", "#5B84B1")

# Generate AI Prompt
st.header("Generated AI Prompt")
prompt = f"A warrior wearing {armor_material.lower()} armor. "
if base_layer != "None":
    prompt += f"Underneath, they wear a {base_layer.lower()} dyed {base_layer_color}. "
if over_armor and "None" not in over_armor:
    prompt += f"Over the armor, they wear {', '.join(over_armor).lower()}, dyed {cloak_color}. "
if helmet != "None":
    prompt += f"They wear a {helmet.lower()} on their head. "
if shoulder_armor != "None":
    prompt += f"Their shoulders are protected by {shoulder_armor.lower()}. "
if engraving_style != "None":
    prompt += f"The armor features {engraving_style.lower()} engravings. "
if decorative_features and "None" not in decorative_features:
    prompt += f"The armor is adorned with {', '.join(decorative_features).lower()}. "
prompt += f"The armor is accented with {armor_accent_color}."

# Display the AI prompt
st.text_area("AI Prompt", value=prompt, height=150)

# Placeholder for future visualization
st.header("Future Armor Visualization")
st.info("Live armor visualization will be implemented in a future version.")
