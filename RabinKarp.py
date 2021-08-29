import tkinter as tk
from tkinter import messagebox


class RabinKarp:
    # // d is the number of characters in the input alphabet
    res = ""
    d = 256
    # index = 0
    prompt = True
    prompt2 = True
    indexes = []
    
    def ifempty(self, t1, r1):
        if (t1 == "\n" or r1 == "\n"):
            tk.messagebox.showwarning("Oho!", "Enter All Required Fields.")
            self.prompt = False

        else:

            self.prompt = True

    def check(self, t1, r1):
        myt1 = t1.strip()
        myr1 = r1.strip()
        if (not myr1.__contains__(myt1)):
            self.prompt2 = False
            tk.messagebox.showerror("Nope!", "Value Does Not Exists.")

    def clear(self, t1, t2, t3, l1):

        t1.delete('1.0', "end")
        t2.config(state="normal")
        t2.delete('1.0', "end")
        t2.config(state="disable")
        t3.delete('1.0', "end")
        l1.configure(text="  ")
        self.indexes.clear()
        self.res = ""
        self.prompt = True
        self.prompt2 = True
    
    def comma_remover(self, t1):
        self.res = self.res[:-2]
        t1.config(state="normal")
        t1.delete('1.0', "end")
        t1.insert(1.0, self.res)
        t1.config(state="disable")

    def highlight_pattern(self,t1, pattern, start="1.0", end="end",regexp=False):

        para= t1.get("1.0", "end").strip()
        t1.delete('1.0', "end")
        t1.insert('1.0', para)


        t1.tag_configure("pat", background="yellow")

        start = t1.index(start)
        end = t1.index(end)
        t1.mark_set("matchStart", start)
        t1.mark_set("matchEnd", start)
        t1.mark_set("searchLimit", end)

        count = tk.IntVar()
        while True:
            index = t1.search(pattern, "matchEnd", "searchLimit",
                                count=count, regexp=regexp)
            if index == "":
                break
            if count.get() == 0:
                break  # degenerate pattern which matches zero-length strings
            t1.mark_set("matchStart", index)
            t1.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            t1.tag_add("pat", "matchStart", "matchEnd")


    def search(self, pat, txt, q, t1, l1):
        mypat = pat.strip()
        mytxt = txt.strip()
        M = len(mypat)
        N = len(mytxt)
        i = 0
        j = 0
        p = 0    # hash value for pattern
        t = 0    # hash value for txt
        h = 1
        self.indexes.clear()
        self.res = ""

        # The value of h would be "pow(d, M-1)% q"
        for i in range(M-1):
            h = (h * self.d) % q

        # Calculate the hash value of pattern and first window
        # of text
        for i in range(M):
            p = (self.d * p + ord(mypat[i])) % q
            t = (self.d * t + ord(mytxt[i])) % q

        # Slide the pattern over text one by one
        for i in range(N-M + 1):
            # Check the hash values of current window of text and
            # pattern if the hash values match then only check
            # for characters on by one
            if p == t:
                # Check for characters one by one
                for j in range(M):
                    if mytxt[i + j] != mypat[j]:
                        break

                j += 1
                # if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
                if j == M:
                    self.res += str(i+1) + ", "
                    t1.config(state="normal")
                    t1.delete('1.0', "end")
                    t1.insert(1.0, self.res)
                    t1.config(state="disable")
                    self.indexes.append(int(i))
                    l1.configure(text=len(self.indexes))

            # Calculate hash value for next window of text: Remove
            # leading digit, add trailing digit
            if i < N-M:
                t = (self.d*(t-ord(mytxt[i])*h) + ord(mytxt[i + M])) % q

                # We might get negative values of t, converting it to
                # positive
                if t < 0:
                    t = t + q
