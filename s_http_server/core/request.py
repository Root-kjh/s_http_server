class Request():
    def __init__(self, request, client_ip):
        lines = request.split('\n')
        self.client_ip = client_ip
        self.method = lines[0].split()[0]
        self.url = lines[0].split()[1]
        self.http_version = lines[0].split()[2]
        self.http_version = lines[0].split()[2]
        self.headers = dict()
        count = 1
        for line in lines[1:]:
            try:
                header = line.split(": ")
                self.headers[header[0]] = header[1].split('\r')[0]
                count+=1
            except:
                self.body = '\n'.join(lines[count:])
                break
        print(self.headers)
        print(self.body)
