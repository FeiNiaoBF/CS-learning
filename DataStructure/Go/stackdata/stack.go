package stackdata

/// Stack Data Structure in Golang

// Stack Data Structure

type node[T any] struct {
	data T
	next *node[T]
}

func newNode[T any](data T) *node[T] {
	return &node[T]{
		data: data,
		next: nil,
	}
}

type Stack[T any] struct {
	top  *node[T]
	size uint
}

func NewStack[T any]() *Stack[T]{
	return &Stack[T] {
		top: nil,
		size: 0,
	}
}

// Public function of stack

// Len get the stack length
func (s *Stack[T]) Len() uint {
	return s.size
}

// Push push data to the top of the stack
func (s *Stack[T]) Push(data T) *Stack[T] {
	newNode := newNode[T](data)
	newNode.next = s.top
	s.top = newNode
	s.size += 1
	return s
}
