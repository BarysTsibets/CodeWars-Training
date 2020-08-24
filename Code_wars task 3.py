"""At a job interview, you are challenged to write an algorithm to check if a given string, s,
can be formed from two other strings, part1 and part2.
The restriction is that the characters in part1 and part2 should be in the same order as in s.
The interviewer gives you the following example and
tells you to figure out the rest from the given test cases."""
"""'codewars' is a merge from 'cdw' and 'oears':
    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears"""


def is_merge(s, part1, part2):
    if s == part1 + part2:
        return True
    if len(part1) + len(part2) == len(s):
        new = ""
        if len(part1) < len(part2):
            for i in range(0, len(part1)):
                new = new + part1[i] + part2[i]
            new = new + part2[len(part1):]
            if s == new:
                return True
            else:
                return False
        elif len(part1) > len(part2):
            for i in range(0, len(part2)):
                new = new + part1[i] + part2[i]
            new = new + part1[len(part2):]
            if s == new:
                return True
            else:
                return False
        elif len(part1) == len(part2):
            for i in range(0, len(part1)):
                new = new + part1[i] + part2[i]
                if s == new:
                    return True
    else:
        return False


s = "codewars"
part1 = "cdwr"
part2 = 'oeas'
print(is_merge(s, part1, part2))















# print(is_merge('codewars', 'code', 'wars'))
#
# print(is_merge('codewars', 'cdwr', 'oeas'))