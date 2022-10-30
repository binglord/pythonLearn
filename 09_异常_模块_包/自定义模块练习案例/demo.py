import util.str_util
from util import file_util as fu

print(util.str_util.str_reverse('Hello world!'))

print(util.str_util.substr('i love learn', 2, 12))

fu.print_file_info("C:\\Users\\Administrator\\Desktop\\新建 文本文档.txt")

fu.append_to_file("C:\\Users\\Administrator\\Desktop\\新建 文本文档.txt", 'loppp')
fu.print_file_info("C:\\Users\\Administrator\\Desktop\\新建 文本文档.txt")
