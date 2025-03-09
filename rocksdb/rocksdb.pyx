cdef extern from "rocksdb/c.h":
    ctypedef struct rocksdb_t:
        pass

    ctypedef struct rocksdb_options_t:
        pass

    rocksdb_t* rocksdb_open(const rocksdb_options_t* options, const char* name, char** errptr)
