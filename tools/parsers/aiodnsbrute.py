from tools.result_parser import ToolResultParser


class Aiodnsbrute(ToolResultParser):
    def parse(self, result, project, creator):
        for line in result.split("\n"):
            if "[+]" in line:
                hostname = line.split(" ")[1].replace("\x1b[0m", "")
                ip = line.split(" ")[-1].replace("\t", "").replace("[", "").replace("]", "").replace("'", "")
                host, _created = self._get_or_create_host(ip, project, creator)
                self._get_or_create_hostname(hostname, host)