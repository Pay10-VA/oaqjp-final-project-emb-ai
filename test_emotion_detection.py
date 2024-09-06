from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        joyResult = emotion_detector('I am glad this happened')
        self.assertEqual(joyResult['dominant_emotion'], 'joy')

        angerResult = emotion_detector('I am really mad about this')
        self.assertEqual(angerResult['dominant_emotion'], 'anger')

        disgustResult = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(disgustResult['dominant_emotion'], 'disgust')

        sadnessResult = emotion_detector('I am so sad about this')
        self.assertEqual(sadnessResult['dominant_emotion'], 'sadness')
        
        fearResult = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(fearResult['dominant_emotion'], 'fear')

unittest.main()
    
    