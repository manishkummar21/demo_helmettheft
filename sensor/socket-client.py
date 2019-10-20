import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
    sio.emit('onVehicleMonitor', {'vehicleID': 'KA02HN3532','helmetdata':True})

@sio.event
def my_message(data):
    print('message received with ', data)

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://192.168.12.40:3000')

sio.wait()