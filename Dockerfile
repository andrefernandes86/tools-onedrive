FROM python:3.8

RUN pip install requests
RUN pip install onedrivesdk
RUN pip install curl
RUN pip install wget

COPY upload_to_onedrive.py /app/upload_to_onedrive.py
RUN mkdir app
RUN cd app
RUN mkdir files_to_upload
RUN cd files_to_upload

RUN curl http://vxvault.net/URL_List.php > urls.txt
RUN wget -i urls.txt --tries=1 --timeout=5

WORKDIR /app

CMD ["python", "upload_to_onedrive.py"]
