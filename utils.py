
import subprocess


def compile_code(language, code):
    if language == 'python':
        return compile_python(code)
    elif language == 'java':
        return compile_java(code)
    elif language == 'c':
        return compile_c(code)
    else:
        raise ValueError(f'Unsupported language: {language}')

def compile_python(code):
    try:
        compiled_code = compile(code, '<string>', 'exec')
        return compiled_code, None
    except Exception as e:
        return None, str(e)

def compile_java(code):
    with open('Main.java', 'w') as f:
        f.write(code)
    compile_result = subprocess.run(['javac', 'Main.java'], text=True, capture_output=True)
    if compile_result.returncode != 0:
        return None, compile_result.stderr
    return 'Main.class', None

def compile_c(code):
    with open('main.c', 'w') as f:
        f.write(code)
    compile_result = subprocess.run(['gcc', '-o', 'main', 'main.c'], text=True, capture_output=True)
    if compile_result.returncode != 0:
        return None, compile_result.stderr
    return 'main', None
