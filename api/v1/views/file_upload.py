""" FIle uplad extension module"""
from flask import Blueprint, send_from_directory, jsonify, request, current_app
from werkzeug.utils import secure_filename
import os

upload_bp = Blueprint('upload_bp', __name__)


def save(uploaded_file):
    """
    save file to upload folder
    """
    filename = secure_filename(uploaded_file.filename)
    file_ext = os.path.splitext(filename)[1]
    if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
        return jsonify({'error': 'File Extension not Allowed'}), 400

    upload_folder = os.path.join(os.path.abspath(
                    os.path.dirname(__file__)), '..', current_app.config['UPLOAD_FOLDER'])
    file_path = os.path.join(upload_folder, filename)
    #file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    uploaded_file.save(file_path)

    return jsonify({'filename': filename})


@upload_bp.route('/upload', methods=['POST'], strict_slashes=False)
def upload():
    """ Handles event file upload """

    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return jsonify({'error': 'No selected file'})

    current_app.config['UPLOAD_FOLDER'] = 'file_uploads/events_img'
    return save(uploaded_file)


@upload_bp.route('/upload/users', methods=['POST'], strict_slashes=False)
def user_upload():
    """
    uplaod user image
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    current_app.config['UPLOAD_FOLDER'] = 'file_uploads/users_img'
    return save(uploaded_file)

@upload_bp.route('/upload/hosts', methods=['POST'], strict_slashes=False)
def host_upload():
        """
        uplaod host image
        """
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        uploaded_file = request.files['file']
        if uploaded_file.filename == '':
            return jsonify({'error': 'No selected file'})

        current_app.config['UPLOAD_FOLDER'] = 'file_uploads/hosts_img'
        return save(uploaded_file)


@upload_bp.route('/download/<filename>', methods=['GET'], strict_slashes=False)
def download(filename):
    """ download event image from folder"""

    current_app.config['UPLOAD_FOLDER'] = 'file_uploads/events_img'
    upload_folder = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), '..', current_app.config['UPLOAD_FOLDER'])
    return send_from_directory(upload_folder, filename)


@upload_bp.route('/download/users/<filename>', methods=['GET'], strict_slashes=False)
def user_download(filename):
    """ 
    download users image from folder
    """

    current_app.config['UPLOAD_FOLDER'] = 'file_uploads/users_img'
    upload_folder = os.path.join(os.path.abspath(
                    os.path.dirname(__file__)), '..', current_app.config['UPLOAD_FOLDER'])
    return send_from_directory(upload_folder, filename)


@upload_bp.route('/download/hosts/<filename>', methods=['GET'], strict_slashes=False)
def host_download(filename):
    """ 
    download host image from folder
    """

    current_app.config['UPLOAD_FOLDER'] = 'file_uploads/hosts_img'
    upload_folder = os.path.join(os.path.abspath(
                    os.path.dirname(__file__)), '..', current_app.config['UPLOAD_FOLDER'])
    return send_from_directory(upload_folder, filename)
