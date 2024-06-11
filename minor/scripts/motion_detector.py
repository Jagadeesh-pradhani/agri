import cv2
import numpy as np
import rospy
from std_msgs.msg import Int32

def main():
    # Initialize the ROS node
    rospy.init_node('motion_detector', anonymous=True)
    motion_pub = rospy.Publisher('/persons', Int32, queue_size=10)
    rate = rospy.Rate(10)  # 10Hz

    # Initialize the video capture
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        rospy.logerr("Error: Could not open video stream.")
        return

    # Initialize the background subtractor
    fgbg = cv2.createBackgroundSubtractorMOG2()

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        
        # If frame read correctly, ret is True
        if not ret:
            rospy.logerr("Failed to grab frame")
            break

        # Apply the background subtractor
        fgmask = fgbg.apply(frame)

        # Find contours in the mask
        contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = 0  # Default is no motion

        # Check if there is any significant contour
        for contour in contours:
            if cv2.contourArea(contour) < 500:
                # Skip small contours to reduce noise
                continue
            motion_detected = 1
            break

        # Publish the motion status
        motion_pub.publish(motion_detected)
        rospy.loginfo(f"Motion detected: {motion_detected}")

        # Display the resulting frame and mask (optional)
        cv2.imshow('Frame', frame)
        cv2.imshow('FG Mask', fgmask)

        # Exit on 'q' key
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

        rate.sleep()

    # Release the capture and destroy all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
