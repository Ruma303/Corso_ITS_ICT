from sys import exit


class Contact:
    name: str = ""
    lastname: str = ""
    phone: str = ""
    email: str = ""

    # def __init__():...

    def __init__(self, n: str, l: str, p: str, e: str):
        self.name = n
        self.lastname = l
        self.phone = p
        self.email = e

    def to_str(self, name: str, lastname: str, phone: str, email: str):
        if self.name == "" or self.name is None:
            return ""

        return (
            f"* {self.lastname}, {self.name}:\n" + f"{self.phone}\n" + f"{self.email}\n"
        )


class Group: ...


def main():
    # c1 = Contact()
    # print(c1)
    c2 = Contact("Mario", "Rossi", "+3976237438", "mario@rossi.it")
    print(c2)
    return 0


if __name__ == "__main__":
    exit(main())
