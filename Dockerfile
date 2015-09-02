FROM ipython/scipyserver

ADD requirements.txt requirements.txt

RUN pip2 install -Ur requirements.txt

# following from https://github.com/ipython/docker-notebook/blob/master/scipyserver/Dockerfile
VOLUME /notebooks
WORKDIR /notebooks

EXPOSE 8888

# You can mount your own SSL certs as necessary here
ENV PEM_FILE /key.pem
# $PASSWORD will get `unset` within notebook.sh, turned into an IPython style hash
ENV PASSWORD Dont make this your default
ENV USE_HTTP 0

ADD notebook.sh /
RUN chmod u+x /notebook.sh

CMD ["/notebook.sh"]


