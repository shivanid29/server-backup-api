import requests
from flask import Flask, jsonify
from flask import request
import paramiko
from paramiko import SSHClient

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False


@app.route('/', methods=['GET'])
def home():
    return 'Hello'


# get details using query parameters
@app.route('/details', methods=['GET'])
def get_details():
    name = request.args['name']
    return jsonify({"status": "success", "name": name}), 200


# get details using path parameter
@app.route('/pdetails/<string:name>', methods=['GET'])
def get_pdetails(name):
    return jsonify({"status": "success", "name": name}), 200


@app.route('/create-backup', methods=['POST'])
def create_backup():
    host = request.args['host']
    port = '22'
    user_name = request.args['user_name']
    password = request.args['password']
    folder_name = request.args['folder_name']
    file_name = request.args['file_name']

    #Commands
    zip_file = "zip -r /home/" + user_name + "/" + file_name + ".zip /home/" + user_name + "/" + folder_name
    tar_file = "tar -cvzf /home/" + user_name + "/" + file_name + ".tar.gz /home/" + user_name + "/" + folder_name

    # ssh connection to the server
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user_name, password)

    choice = request.args['file_format']

    if choice == "tar":
        stdin, stdout, stderr = ssh.exec_command(tar_file)
        stdout.readlines()
        path_readyto_download = host + "/" + user_name + "/" + file_name + ".tar.gz"
        return jsonify({"status": "success", "path": path_readyto_download, "file_name": file_name + ".tar.gz"}), 200

    elif choice == "zip":
        stdin, stdout, stderr = ssh.exec_command(zip_file)
        stdout.readlines()
        path_readyto_download = host + "/" + user_name + "/" + file_name + ".zip"
        return jsonify({"status": "success", "path": path_readyto_download, "file_name": file_name + ".zip"}), 200

    else:
        return jsonify({"status": "error", "message": "Please enter a correct file format"}), 500


app.run()
