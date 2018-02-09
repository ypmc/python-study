def echo_bar(self):
    return self.bar


Foo = type('Foo', (), {'bar': True})

FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})

print(FooChild.bar)
print(hasattr(FooChild, 'echo_bar'))
print(FooChild.__class__)

child = FooChild()
print(child.echo_bar())
print(child.__class__)
print(child.__class__.__class__)
