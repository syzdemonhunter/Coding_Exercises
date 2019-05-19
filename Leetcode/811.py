# https://leetcode.com/problems/subdomain-visit-count/
# T: O(n)
# T: O(n*k)

class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        count = {}
        for domain in cpdomains:
            visits = int(domain.split()[0])
            domains_all = domain.split()[1]
            domain_list = domains_all.split('.')
            
            top = domain_list[-1]
            sec = domain_list[-2] + '.' + top
            
            count[top] = count[top] + visits if top in count else visits
            count[sec] = count[sec] + visits if sec in count else visits
            
            if domain.count('.' ) == 2:
                count[domains_all] = \
                count[domains_all] + vistis if domains_all in count else visits
                
        return [str(v) + ' ' + k for k, v in count.items()]
            