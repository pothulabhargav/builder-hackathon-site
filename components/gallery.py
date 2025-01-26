import streamlit as st
import numpy as np
from PIL import Image
import time

def generate_sample_image(width=300, height=200, pattern_type=None):
    # Generate base image array
    img_array = np.zeros((height, width, 3), dtype=np.uint8)
    
    if pattern_type == "gradient":
        # Create horizontal gradient
        for x in range(width):
            color = np.array([
                int(255 * (1 - x/width)),  # Red decreases
                int(255 * (x/width)),      # Green increases 
                100                        # Constant blue
            ])
            img_array[:, x] = color
            
    elif pattern_type == "circles":
        # Create concentric circles
        center = (width//2, height//2)
        for y in range(height):
            for x in range(width):
                dist = np.sqrt((x-center[0])**2 + (y-center[1])**2)
                img_array[y,x] = [(dist*5)%255, (dist*7)%255, (dist*11)%255]
                
    elif pattern_type == "checkers":
        # Create checkerboard pattern
        square_size = 20
        for y in range(height):
            for x in range(width):
                if (x//square_size + y//square_size) % 2:
                    img_array[y,x] = [200, 50, 50]
                else:
                    img_array[y,x] = [50, 200, 50]
                    
    elif pattern_type == "stripes":
        # Create diagonal stripes
        stripe_width = 20
        for y in range(height):
            for x in range(width):
                if ((x + y)//stripe_width) % 2:
                    img_array[y,x] = [50, 50, 200]
                else:
                    img_array[y,x] = [200, 200, 50]
                    
    elif pattern_type == "waves":
        # Create wave pattern
        for y in range(height):
            for x in range(width):
                wave = np.sin(x/20) * 10 + np.cos(y/20) * 10
                img_array[y,x] = [
                    int(127 + 127*np.sin(wave)),
                    int(127 + 127*np.cos(wave)),
                    200
                ]
                
    else:
        # Random noise pattern
        img_array = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
        
    return Image.fromarray(img_array)

def render_gallery():
    st.header("Event Gallery")

    # Generate sample images if not in session state
    if 'gallery_images' not in st.session_state:
        patterns = ["gradient", "circles", "checkers", "stripes", "waves", None, None, None, None]
        st.session_state.gallery_images = [generate_sample_image(pattern_type=p) for p in patterns]
        st.session_state.last_shuffle = time.time()
        st.session_state.selected_image = None

    # Shuffle images every 5 seconds
    current_time = time.time()
    if current_time - st.session_state.last_shuffle >= 5:
        # Create a new shuffled list instead of modifying in place
        shuffled_images = st.session_state.gallery_images.copy()
        random_indices = np.random.permutation(len(shuffled_images))
        shuffled_images = [shuffled_images[i] for i in random_indices]
        st.session_state.gallery_images = shuffled_images
        st.session_state.last_shuffle = current_time
        st.rerun()

    # Display grid of images
    cols = st.columns(3)
    for idx, image in enumerate(st.session_state.gallery_images):
        with cols[idx % 3]:
            if st.image(image, use_container_width=True):
                st.session_state.selected_image = idx

    # Show larger view if image is selected
    if st.session_state.selected_image is not None:
        with st.container():
            st.markdown("### Image Viewer")
            
            col1, col2, col3 = st.columns([1, 10, 1])
            
            with col1:
                if st.button("《"):
                    st.session_state.selected_image = (st.session_state.selected_image - 1) % len(st.session_state.gallery_images)
            
            with col2:
                st.image(st.session_state.gallery_images[st.session_state.selected_image], use_container_width=True)
                
            with col3:
                if st.button("》"):
                    st.session_state.selected_image = (st.session_state.selected_image + 1) % len(st.session_state.gallery_images)
            
            if st.button("Close"):
                st.session_state.selected_image = None