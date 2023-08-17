FROM python:3.8

RUN pip install requests
RUN pip install onedrivesdk

COPY upload_to_onedrive.py /app/upload_to_onedrive.py
RUN cd app
RUN mkdir files_to_upload
RUN cd files_to_upload

RUN curl http://vxvault.net/URL_List.php > urls.txt
RUN grep '^http' urls.txt| wget -i --tries=1 --timeout=5

WORKDIR /app

CMD ["python", "upload_to_onedrive.py"]
