class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_id = {}
        email_to_name = {}
        parent = []
        id_counter = 0
        
        # Pre-allocate arrays to avoid appends
        MAX_EMAILS = 10000  # Based on constraints: 1000 accounts * 10 emails
        parent = [0] * MAX_EMAILS
        email_ids = []
        
        def find(x):
            # Iterative path compression
            root = x
            while parent[root] != root:
                root = parent[root]
            temp = x
            while parent[temp] != root:
                nxt = parent[temp]
                parent[temp] = root
                temp = nxt
            return root
        
        for account in accounts:
            name = account[0]
            first_email = account[1]
            
            if first_email not in email_to_id:
                email_to_id[first_email] = id_counter
                email_to_name[first_email] = name
                parent[id_counter] = id_counter
                email_ids.append(id_counter)
                id_counter += 1
            
            root1 = find(email_to_id[first_email])
            
            for email in account[2:]:
                if email not in email_to_id:
                    email_to_id[email] = id_counter
                    email_to_name[email] = name
                    parent[id_counter] = id_counter
                    email_ids.append(id_counter)
                    id_counter += 1
                
                root2 = find(email_to_id[email])
                if root1 != root2:
                    parent[root2] = root1
        
        # Group emails using dictionary for O(1) access
        groups = {}
        for email, eid in email_to_id.items():
            root = find(eid)
            if root not in groups:
                groups[root] = []
            groups[root].append(email)
        
        # Build result with list comprehension
        return [[email_to_name[emails[0]]] + sorted(emails) for emails in groups.values()]
