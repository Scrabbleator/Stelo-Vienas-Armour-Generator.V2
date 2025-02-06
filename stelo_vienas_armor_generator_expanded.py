import streamlit as st

# Set App Title
st.title("Stelo Vienas Armor Generator")
st.subheader("Create and record your ultimate armor combinations!")

# Sidebar: Preset Configurations
st.sidebar.header("Preset Configurations")
preset = st.sidebar.selectbox(
    "Choose a Preset",
    ["Custom", "Knight", "Rogue", "Noble"]
)

# Sidebar: Layered Customization
st.sidebar.header("Armor Customization")

# Base Layer Options
base_layer = st.sidebar.selectbox(
    "Base Layer (Under Armor)",
    ["None", "Gambeson", "Leather Jerkin", "Padded Doublet"]
)

# Under Armor Options
under_armor = st.sidebar.selectbox(
    "Under Armor",
    ["None", "Chainmail Hauberk", "Brigandine", "Scale Mail"]
)

# Over Armor Options
over_armor = st.sidebar.multiselect(
    "Over Armor",
    ["None", "Hooded Tunic", "Heraldic Surcoat", "Fur-Lined Mantle", "Flowing Cape"]
)

# Helmet Options
helmet = st.sidebar.selectbox(
    "Helmet",
    ["None", "Great Helm", "Bascinet", "Open-Faced Helm", "Barbute"]
)

# Armor Material Options
armor_material = st.sidebar.selectbox(
    "Armor Material",
    ["Steel", "Gold", "Blackened Iron", "Mithril", "Hardened Leather", "Bone"]
)

# Color Customization with Color Wheel
st.sidebar.header("Color Customization")
base_layer_color = st.sidebar.color_picker("Base Layer Color", "#B87333")
armor_accent_color = st.sidebar.color_picker("Armor Accent Color", "#FFD700")
cloak_color = st.sidebar.color_picker("Cloak or Over Armor Color", "#5B84B1")

# Scratch-Pad for Configurations
st.sidebar.header("Scratch-Pad")
scratch_pad = st.sidebar.text_area("Record Your Previous Configurations", "")

# Generate AI Prompt
st.header("Generated AI Prompt")
prompt = f"A warrior wearing {armor_material.lower()} armor. "
if base_layer != "None":
    prompt += f"They wear a {base_layer.lower()} dyed {base_layer_color}. "
if under_armor != "None":
    prompt += f"Beneath, they have {under_armor.lower()}. "
if over_armor and "None" not in over_armor:
    prompt += f"Over the armor, they wear {', '.join(over_armor).lower()} dyed {cloak_color}. "
if helmet != "None":
    prompt += f"They wear a {helmet.lower()} on their head. "

st.text_area("AI Prompt", value=prompt, height=150)

# Scratch-Pad Display
st.header("Scratch-Pad for Previous Configurations")
st.write("Use this space to record your configurations:")
st.text_area("Scratch-Pad", value=scratch_pad, height=200)
