###### Namespace

- A `namespace` (sometimes called a context) is a naming system for makng names unique to avoid ambiguity
    * Everybody knows a namespacing system from everyday life
        * Naming of people in the first name and family name
        * A network
            * Each network device (workstation, server, printer) needs a unique name and address
        * Directory structure of filesystems
            * The same filename can be used in different directories, The paths can be uniquely accessed via the pathnames
- Many programming languages use namespaces or contexts for identifiers
    * An identifier defined in a namespace is associated with that namespace
    * This way, the same identifier can be independently defined in multiple namespaces


- Namespaces in Python are implemented as Python dictionaries
    * This means that they are defined by a mapping from names (the keys of the dictionaries) to objects (the values of the dictionary)
    * The user doesn't have to know this to write a Python program and when using namespaces


- Some namespaces in Python
    * `Global names` of a module
    * `Local names` in a function or method invocation
    * `Built-in names`
        * This namespace contains built-in functions (abs(), cmp()) and built in exception names


###### Lifetime of a Namespace

- Not every namespace, which may be used in a script or program is accessible (or alive) at any moment during the execution of the script
- Namespaces have different lifetimes b/c they are often created at different points in time

- There is one namespace which is present from beginning to end
    * The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted

- The global namespace of a module is generated when the module is read in
- Module namespaces normally last until the script ends
    * i.e. the interpreter quits

- When a function is called, a local namespace is created for this function
- The namespace is deleted either if 
    * The function ends (it returns)
    * The function raises an exception which is not dealt with within the function

###### Scopes

- A scope refers to a region of a program where a namespace can be directly accessed
    * i.e. w/o using a namespace prefix
- In other words:
    * The scope of a name is the area of a program where this name can be unambiguously used, for example, within a function
- A name's namespace is identical to it's scope
- Scopes are defined statically, but they are used dynamically

- During program execution, there are the following nested scopes available
    * The innermost scope is searched first and it contains the local names
    * The scopes of any enclosing funcitons, which ar searched starting with the nearest enclosing scope
        * If a function is wrapped inside of another function
    * The next-to-last scope contains the current module's global names
        * Uppermost level of the executing scripts itself
    * The outermost scope, which is searched last, is the namespace containing the built-in names


- 