# 🖼 Image Processor App

An interactive **Image Processing Web Application** built with [Streamlit](https://streamlit.io/).  
It allows users to upload an image, apply different **processing techniques**, and visually compare the **original vs. processed image** in real time.

---

## 🚀 Features
- 📤 Upload **JPG, JPEG, PNG** images  
- 🎛 Apply various image processing techniques:
  - ✅ Thresholding  
  - ✅ Brightness (Power Law Transformation)  
  - ✅ Contrast Enhancement (Histogram Equalization)  
  - ✅ Gaussian Blur  
  - ✅ Edge Detection (Canny)  
  - ✅ Salt & Pepper Noise with Median Denoising  
  - ✅ Complement Image (Inversion)  
  - ✅ JPEG Compression with file size display & download  
- 🔍 **Side-by-Side Image Comparison** (powered by `streamlit-image-comparison`)  
- 📥 Download option for **compressed JPEG**  

---

## 🛠 Tech Stack
- **Frontend / UI:** Streamlit  
- **Image Processing:** OpenCV, NumPy, scikit-image, Pillow  
- **Visualization:** streamlit-image-comparison  

---

## 📦 Installation & Setup

Clone the repository:

```bash
git clone https://github.com/your-username/image-processor-app.git
cd image-processor-app
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## 📂 Project Structure
```
📦 image-processor-app
 ┣ 📜 app.py                # Main Streamlit app
 ┣ 📜 requirements.txt      # Python dependencies
 ┣ 📜 README.md             # Documentation
```

---

## 🖼 Demo
After running, open your browser at `http://localhost:8501` to use the app.

---

## 🤝 Contributing
Pull requests are welcome!  
If you’d like to add new image processing techniques, feel free to fork this repo and submit a PR.  

---

## 📜 License
This project is licensed under the **MIT License**.
