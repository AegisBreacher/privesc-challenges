FROM debian:bookworm-slim

#Install SSH Server
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    openssh-server \
    libcap2-bin \
    curl wget sudo less 


#Configure SSH (Cant run as Daemon if this doenst exit)
RUN mkdir /var/run/sshd

RUN cp /sbin/getcap  /usr/bin/getcap

# --- System Configuration --------
#Add a User
RUN useradd -ms /bin/bash aegis && echo aegis:aegis | chpasswd

COPY .root.txt /root/root.txt
RUN chmod 600 /root/root.txt

# ----- Custom 
RUN apt-get install --no-install-recommends -y \
    perl \
    cowsay

COPY sudoers /etc/sudoers

# PORTS AND BASIC COMMAND
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]