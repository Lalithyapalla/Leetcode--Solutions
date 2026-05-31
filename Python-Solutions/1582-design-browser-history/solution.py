class BrowserHistory:
    class Node:
        def __init__(self, url: str):
            self.url = url
            self.prev = None
            self.next = None

    def __init__(self, homepage: str):
        self.cur = self.Node(homepage)

    def visit(self, url: str) -> None:
        newnode = self.Node(url)
        self.cur.next = newnode
        newnode.prev = self.cur
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.prev != None:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next != None:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
