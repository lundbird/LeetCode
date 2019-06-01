class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        filtered_emails = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.replace(".","")
            plus_index = local.find("+")
            if plus_index >= 0:
                local = local[:plus_index]
            filtered_emails.add(local + "@" + domain)
        return len(filtered_emails)