# VisionStack_PPEDetection

1. Project Title
- Application Name: PPE Kit Detection 
- Short Description: A Flask-based application that utilizes OpenCV for real-time detection of Personal Protective Equipment (PPE) on individuals.

2. Overview
- Purpose:
      - To detect if a  person is wearing the Personal Protective Equipments (PPE kits) while working on the Factory Floor.
- Functionality:
      - PPE kit detection using the YOLO v8 algorithm from the Ultralytics library.
      - The model is able to track if a person (Factory Worker) is wearing safety equipments like Helmet,Safety Vest, Safety Boots, Glasses and Gloves.
      - The model highlights the equipment wore by the person in a green colour and displays a text indicating the equipment.
      - The model displays the equipment only after a certian level of confidence which is dynamic and can be changed according to the need.
      - The model is deployed on localhost on port 5000 using the Flask API.
  
3. Installation Instructions
- Prerequisites:
      - Python version 3
      - Flask version 3
      - OpenCV-Python library
  
- Installation Steps:
      - Clone/download the repository
      - Set up a Python virtual environment
      - Install required Python packages: `pip install -r requirements.txt`

4. Usage
- Instructions to start the server:
      - Run the flask_PPE.py for Video stream or flask_PPE_Photo.py for a single frame from the Video stream (or photo).
      - Copy the IP address from the terminal and paste it into a browser window and add `/video_feed/<item>` here replace `/<item>` with the safety equipment you want to check for (ex 
        Helmet) and for checking for all the equipments at once replace `/<item>` with `/all`
      - For a single frame instead of `/video_feed/<item>` do `/photo/<item>`
- Output:
       - The output of the model can be viewed on a browser in a video format and on the terminal in text format.
       - The output window "Frame" consists of the original video plus the detected items from a safety[] list, their confidence level, Number of people and the Frame Rate of the application.
       - Same items can also be viewed in the terminal.

5. Code Structure
- Modules and Packages: Description of the project's directory structure and an overview of the main modules and packages.
        - `flask_PPE.py` and `flask_PPE_Photo.py`  - The main Flask application files.
        - `PPE_rec.py` and `PPE_rec_p.py` - Modules for PPE detection using OpenCV.
        - `templates/` - Folder containing HTML files for the web interface.
        
6. API Reference
- Endpoints:
        - `/video_feed/<item>` and `/photo/<item>` - Endpoint for processing images and returning detection results.

6. Performance
    -  The average FPS for AMD Ryzen 5, GTX 1650, 16 GB RAM is 50 FPS
    -  The average FPS for Jetson Nano is    FPS
