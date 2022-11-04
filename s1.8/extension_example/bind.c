#include "libmypy.h"

/* Тут пишем метаинформацию о модуле для интерпретатора питона */

char hellofunc_docs[] = "Hello world description.";

/* PyMethodDef - определяем методы в нашем модуле */
PyMethodDef helloworld_funcs[] = {
	{	"hello", // имя функции которая будет вызвана в питоне
		(PyCFunction)hello, // имя функции в С
		METH_NOARGS, // сообщаем, что у нас нет аргументов
		hellofunc_docs}, // документация
	{	NULL}
};

char helloworldmod_docs[] = "This is hello world module.";

/* PyModuleDef - информация о самом модуле
    https://docs.python.org/3/c-api/module.html?highlight=pymoduledef#c.PyModuleDef
 */
PyModuleDef helloworld_mod = {
	PyModuleDef_HEAD_INIT,
	"helloworld", // имя
	helloworldmod_docs, // документация
	-1, // объем памяти для хранения состояния программы
	helloworld_funcs // методы, которые будут в модуле
};

/* при импорте вызывается PyMODINIT_FUNC
    PyModule_Create()вернет новый объект модуля типа PyObject *
 */
PyMODINIT_FUNC PyInit_helloworld(void) {
	return PyModule_Create(&helloworld_mod);
}