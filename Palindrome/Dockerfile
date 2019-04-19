FROM alpine:3.9

LABEL maintainer="<Sunil Nagavelli>sunilngvli@gmail.com"

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN addgroup -S appgroup && adduser -S appusr -G appgroup -h /home/appusr &&\
		mkdir /home/appusr/scripts

COPY IsPalindrome.py /home/appusr/scripts

WORKDIR /home/appusr/scripts

RUN chmod 755 IsPalindrome.py

ENTRYPOINT [ "python", "./IsPalindrome.py" ]
