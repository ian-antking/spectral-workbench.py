# spectral-workbench.py
Capture and upload a spectrum to spectral workbench using raspberry pi.

Designed to work with the lego spectrometer from publiclab.org, details on how to build on can be found here:

https://publiclab.org/w/lego-spectrometer

The script can be initailised over SSH, but still requires the RPi to be connected to a monitor in order to show the camera preview. This will not work over a remote desktop.

What is does:

  User inputs label for the spectrum.
  
  The script will show a preview of the spectrum to be caputured, before saving the image to /home/pi/Pictures with the file name set as the spectrum label.
  
  The middle row of pixels are then extracted and base64 encoded as a dataurl. The extracted pixels are also saved to the Pictures folder. 
  
  The encoded image and identifying information are uploded as a POST request to spectral workbench. The response code is then printed.


Areas for improvement:

  Overlaying a guide across the camera preview to show where the specrum will be extracted for uploading.
  
  Do the extracted pixels need to be saved as an image before being encoded? Early versions required the image to be opened with the 'rb' perameter or encoding to fail. Any way round this would make the code shorter.
  
