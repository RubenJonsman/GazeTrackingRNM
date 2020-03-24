import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
sentence = []

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it  
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    if left_pupil is None:
        pass
    else:
        left = list(left_pupil)

    def FindPoint():     # x2,y2,x2,y2
        xA, yA, xA2, yA2 = 0, 0, 10, 8
        xB, yB, xB2, yB2 = 0, 0, 10, 8
        xC, yC, xC2, yC2 = 0, 0, 10, 8
        xD, yD, xD2, yD2 = 0, 0, 10, 8
        xE, yE, xE2, yE2 = 0, 0, 10, 8
        xF, yF, xF2, yF2 = 0, 0, 10, 8
        xG, yG, xG2, yG2 = 0, 0, 10, 8
        xH, yH, xH2, yH2 = 0, 0, 10, 8
        xI, yI, xI2, yI2 = 0, 0, 10, 8
        xJ, yJ, xJ2, yJ2 = 0, 0, 10, 8
        xK, yK, xK2, yK2 = 0, 0, 10, 8
        xL, yL, xL2, yL2 = 0, 0, 10, 8
        xM, yM, xM2, yM2 = 0, 0, 10, 8
        xN, yN, xN2, yN2 = 0, 0, 10, 8
        xO, yO, xO2, yO2 = 0, 0, 10, 8
        xP, yP, xP2, yP2 = 0, 0, 10, 8
        xQ, yQ, xQ2, yQ2 = 0, 0, 10, 8
        xR, yR, xR2, yR2 = 0, 0, 10, 8
        xS, yS, xS2, yS2 = 0, 0, 10, 8
        xT, yT, xT2, yT2 = 0, 0, 10, 8
        xU, yU, xU2, yU2 = 0, 0, 10, 8
        xV, yV, xV2, yV2 = 0, 0, 10, 8
        xW, yW, xW2, yW2 = 0, 0, 10, 8
        xX, yX, xX2, yX2 = 0, 0, 10, 8
        xY, yY, xY2, yY2 = 0, 0, 10, 8
        xZ, yZ, xZ2, yZ2 = 0, 0, 10, 8
        xAE, yAE, xAE2, yAE2 = 0, 0, 10, 8
        xOE, yOE, xOE2, yOE2 = 0, 0, 10, 8
        xAA, yAA, xAA2, yAA2 = 0, 0, 10, 8
        xSpace, ySpace, xSpace2, ySpace2 = 0, 0, 10, 8
        xSlet, ySlet, xSlet2, ySlet2 = 0, 0, 10, 8


        if left[0] > xA and left[0] < xA2 and left[1] > yA and left[1] < yA2:
            s = ["A"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xB and left[0] < xB2 and left[1] > yB and left[1] < yB2:
            s = ["B"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xC and left[0] < xC2 and left[1] > yC and left[1] < yC2:
            s = ["C"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xD and left[0] < xD2 and left[1] > yD and left[1] < yD2:
            s = ["D"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xE and left[0] < xE2 and left[1] > yE and left[1] < yE2:
            s = ["E"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xF and left[0] < xF2 and left[1] > yF and left[1] < yF2:
            s = ["F"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xG and left[0] < xG2 and left[1] > yG and left[1] < yG2:
            s = ["G"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xH and left[0] < xH2 and left[1] > yH and left[1] < yH2:
            s = ["H"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xI and left[0] < xI2 and left[1] > yI and left[1] < yI2:
            s = ["I"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xJ and left[0] < xJ2 and left[1] > yJ and left[1] < yJ2:
            s = ["J"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xK and left[0] < xK2 and left[1] > yK and left[1] < yK2:
            s = ["K"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xL and left[0] < xL2 and left[1] > yL and left[1] < yL2:
            s = ["L"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xM and left[0] < xM2 and left[1] > yM and left[1] < yM2:
            s = ["M"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xN and left[0] < xN2 and left[1] > yN and left[1] < yN2:
            s = ["N"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xO and left[0] < xO2 and left[1] > yO and left[1] < yO2:
            s = ["O"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xP and left[0] < xP2 and left[1] > yP and left[1] < yP2:
            s = ["P"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xQ and left[0] < xQ2 and left[1] > yQ and left[1] < yQ2:
            s = ["Q"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xR and left[0] < xR2 and left[1] > yR and left[1] < yR2:
            s = ["R"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xS and left[0] < xS2 and left[1] > yS and left[1] < yS2:
            s = ["S"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xT and left[0] < xT2 and left[1] > yT and left[1] < yT2:
            s = ["T"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xU and left[0] < xU2 and left[1] > yU and left[1] < yU2:
            s = ["U"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xV and left[0] < xV2 and left[1] > yV and left[1] < yV2:
            s = ["V"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xW and left[0] < xW2 and left[1] > yW and left[1] < yW2:
            s = ["W"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xX and left[0] < xX2 and left[1] > yX and left[1] < yX2:
            s = ["X"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xY and left[0] < xY2 and left[1] > yY and left[1] < yY2:
            s = ["Y"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xZ and left[0] < xZ2 and left[1] > yZ and left[1] < yZ2:
            s = ["Z"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xAE and left[0] < xAE2 and left[1] > yAE and left[1] < yAE2:
            s = ["Æ"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xOE and left[0] < xOE2 and left[1] > yOE and left[1] < yOE2:
            s = ["Ø"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xAA and left[0] < xAA2 and left[1] > yAA and left[1] < yAA2:
            s = ["Å"]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xSpace and left[0] < xSpace2 and left[1] > ySpace and left[1] < ySpace2:
            s = [" "]
            if gaze.is_blinking():
                sentence.append(s)
            return True
        elif left[0] > xSlet and left[0] < xSlet2 and left[1] > ySlet and left[1] < ySlet2:
            if gaze.is_blinking():
                sentence.pop()
            return True

        else:
            return False

    cv2.imshow("Demo", frame)
    if cv2.waitKey(1) == 27:
        break
