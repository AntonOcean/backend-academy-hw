#include <Python.h>
#include "libmypy.h"

/* подключаем https://docs.python.org/3/c-api/intro.html#include-files
    для использования https://docs.python.org/3/c-api/index.html
*/

PyObject * hello(PyObject * self) {
    /* Возвращаем строчку */
	return PyUnicode_FromFormat("Hello C extension!");

	/* А можно прямо тут вызывать принт
	 	printf("Hello C extension!");
	 */
}