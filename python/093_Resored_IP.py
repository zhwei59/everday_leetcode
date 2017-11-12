class Solution(object):
    def juge(self, length, s, ips):
        if not s:
            if length == 4:
                self.result.append('.'.join(ips))
            return
        elif length == 4:
            return
        self.juge(length + 1, s[1:], ips + [s[:1]])
        if s[0] != '0':
            if len(s) >= 2:
                self.juge(length + 1, s[2:], ips + [s[:2]])
            if len(s) >= 3 and int(s[:3]) <= 255:
                self.juge(length + 1, s[3:], ips + [s[:3]])

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = []
        self.juge(0, s, [])
        return self.result