import cv2
import os

def extract_frames(video_path):
    # Check if the video file exists
    if not os.path.exists(video_path):
        print("Video file not found.")
        return

    # Directory to store frames
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_directory = f"{video_name}_frames"
    os.makedirs(output_directory, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Save each frame as a PNG file
        frame_filename = os.path.join(output_directory, f"{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()

    print(f"Extracted {frame_count} frames to '{output_directory}'.")

if __name__ == "__main__":
    video_path = ""  # Replace with your video file path
    extract_frames(video_path)
