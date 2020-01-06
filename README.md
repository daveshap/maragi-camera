# MARAGI Camera

Simple microservice for grabbing and publishing video images into the MARAGI server

# Example

```python
import maragi-camera
service = maragi-camera.Service()
service.list_cameras()
service.claim_camera(1)
service.fps = 4
service.add_server(ip='192.168.0.123', port='8686')
service.list_servers()
service.run()```
