import tkinter as tk
import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
fps=60
class VideoPlayer:
    def __init__(self, root, video_path):
        self.container = ctk.CTkFrame(root)
        self.container.pack(expand=True, fill="both")

        # Open the video file
        self.cap = cv2.VideoCapture(video_path)

        # Get video properties
        self.width = int(self.cap.get(3))
        self.height = int(self.cap.get(4))

        # Create a Canvas to display video frames
        self.canvas = tk.Canvas(self.container, width=self.width, height=self.height)
        self.canvas.pack()        

        # Play the video
        self.play_video()

    def play_video(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert the OpenCV BGR image to RGB
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert the image to a PhotoImage
            photo = ImageTk.PhotoImage(Image.fromarray(img))

            # Update the Canvas with the new frame
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.photo = photo

            # Repeat the process after 33 milliseconds (30 frames per second)
            self.container.after(fps, self.play_video)
        else:
            # Release the video capture object when the video is finished
            self.cap.release()

def create_overlay_label(root, container):
    # Create a label to overlay on the video
    overlay_label = ctk.CTkFrame(container,)
    overlay_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    video_path = "bgv.mp4"  # Replace with the path to your video file
    root = ctk.CTk()
    player = VideoPlayer(root, video_path)
    create_overlay_label(root, player.container)
    
    root.mainloop()
