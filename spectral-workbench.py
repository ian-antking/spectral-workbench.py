import picamera
import time
from PIL import Image
import requests
import base64
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

camera = picamera.PiCamera(framerate = 10)

#camera settings may differ depending on device
camera.rotation = 270
camera.iso =1600
camera.shutter_speed = 8000000000
camera.resolution = (640, 480)
camera.zoom = (0.25, 0.25, 0.5, 0.5)

#take the initial spectral reading
def take_reading(sample_name):
        camera.start_preview()
        time.sleep(10)
  
#change file path depending on preference
        camera.capture('/home/pi/Pictures/%s.png' % sample_name)
        return('/home/pi/Pictures/%s.png' % sample_name)
        camera.stop_preview()

#process and encode image for upload
def process_image(image_path):
        img = Image.open(image_path)
        img_width = img.size[0]
        half_height = img.size[1]/2
        img2 = img.crop((0, half_height, img_width, half_height + 1))
        img2.save('/home/pi/Pictures/%s_processed.png' % sample_name)
        #open processed image in binary
        with open('/home/pi/Pictures/%s_processed.png' % sample_name, 'rb') as image_file:
		encoded_image = base64.b64encode(image_file.read())
 	return encoded_image

def workbench_upload(encoded_image):
	url = 'https://spectralworkbench.org/spectrums'
	
	#replace with your api token
	api_token = 'your api token here'
	
	payload = {
	'spectrum':{
		'title': sample_name
		},
	'dataurl': encoded_image,
	#'token': api_token
	}
	
	try:
		r = requests.post(url, data = payload, verify=False)
		print(r.status_code)
	except requests.exceptions.RequestException as e:
		print(e)
		
		
sample_name = input('Enter sample name:')

workbench_upload(process_image(take_reading(sample_name)))


