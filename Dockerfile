FROM python:3.9.19-alpine3.20
WORKDIR /app
COPY /PortScanD.py /app/portscan.py
RUN pip install netaddr
ENTRYPOINT ["python", "portscan.py"]
