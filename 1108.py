class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace('.', '[.]')       # using the replace method of python
        return address
