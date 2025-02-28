import os
import cv2
from datetime import datetime

def extract_frames(video_path, output_dir):
    """
    Extract frames from a video at a rate of 1 frame per second.
    
    Args:
        video_path (str): Path to the video file
        output_dir (str): Directory to save extracted frames
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get video filename without extension
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    
    # Open the video
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    
    print(f"Video: {video_path}")
    print(f"FPS: {fps}")
    print(f"Duration: {duration:.2f} seconds")
    
    # Extract 1 frame per second
    for sec in range(int(duration)):
        # Set frame position (convert seconds to frame number)
        frame_position = int(sec * fps)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_position)
        
        # Read frame
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Save frame
        frame_path = os.path.join(output_dir, f"{video_name}_sec{sec:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        
    # Release resources
    cap.release()
    print(f"Extraction completed. {int(duration)} frames saved to {output_dir}")

def process_video_directory(video_dir, output_base_dir):
    """
    Process all videos in a directory.
    
    Args:
        video_dir (str): Directory containing videos
        output_base_dir (str): Base directory to save frames
    """
    # Create output base directory if it doesn't exist
    if not os.path.exists(output_base_dir):
        os.makedirs(output_base_dir)
    
    # Process each video file
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov']
    for filename in os.listdir(video_dir):
        file_path = os.path.join(video_dir, filename)
        if os.path.isfile(file_path) and os.path.splitext(filename)[1].lower() in video_extensions:
            # Create output directory for this video
            video_name = os.path.splitext(filename)[0]
            output_dir = os.path.join(output_base_dir, video_name)
            
            # Extract frames
            extract_frames(file_path, output_dir)

def main():
    # Directory paths
    video_dir = "Video"
    output_base_dir = "Foto"
    
    # Process all videos
    process_video_directory(video_dir, output_base_dir)
    
    # Or process a specific video
    extract_frames("Video/pal.mp4", "Foto/pal")

if __name__ == "__main__":
    start_time = datetime.now()
    print(f"Starting video frame extraction at {start_time}")
    main()
    end_time = datetime.now()
    print(f"Process completed in {end_time - start_time}")