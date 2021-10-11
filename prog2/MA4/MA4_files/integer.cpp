#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib(int)
	private:
		int val;
		int fib_val
	};
 
Integer::Integer(int n){
	val = n;
	}
 
int Integer::get(){
	return val;
	}
 
void Integer::set(int n){
	val = n;
	fib_val = val;
	}

int Integer::fib(){
	return _fib(fib_val);
	}

int Integer::_fib(int n){
	fib_val = n;
	if (fib_val<=1)
		return fib_val;
	return _fib(n-1) + _fib(n-2);
}

extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	int Integer_fib(Integer* integer) {integer->fib();}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}