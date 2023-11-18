from unittest import TestCase
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Ivan", {'A': ["some notes", ]})

    def test_student_initializing_init_when_no_courses(self):
        self.student = Student("Ivan")
        self.assertEqual(self.student.name, 'Ivan')
        self.assertDictEqual(self.student.courses, {})

    def test_student_instance_init_with_courses(self):
        self.assertEqual(self.student.name, 'Ivan')
        self.assertDictEqual(self.student.courses, {'A': ["some notes", ]})

    def test_student_try_enroll_existing_course(self):
        result = self.student.enroll('A',['some A notes'])
        expected = "Course already added. Notes have been updated."
        self.assertEqual(result, expected)

    def test_student_enroll_course_without_3rd_parameter(self):
        result = self.student.enroll('B', ['some B notes',])
        expected = "Course and course notes have been added."
        self.assertEqual(result, expected)
        self.assertEqual(self.student.courses['B'], ['some B notes'],)

    def test_student_enroll_course_successfully_with_notes(self):
        result = self.student.enroll('B', ['some new notes', ], 'Y')
        expected = "Course and course notes have been added."
        self.assertEqual(result, expected)
        self.assertEqual(self.student.courses['B'], ['some new notes'], )

    def test_student_enroll_course_successfully_no_notes(self):
        result = self.student.enroll('C', ['some C notes'], 'N')
        expected = "Course has been added."
        self.assertEqual(result, expected)
        self.assertEqual(self.student.courses['C'], [])

    def test_add_course_notes_if_course_exists(self):
        result = self.student.add_notes("A", 'some new notes')
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student.courses['A'], ['some notes', 'some new notes'])

    def test_add_course_notes_if_course_not_exists(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("B", 'some new notes')
        expected = "Cannot add notes. Course not found."
        self.assertEqual(str(ex.exception), expected)

    def test_leave_course_if_course_exists(self):
        result = self.student.leave_course("A")
        self.assertEqual(result, "Course has been removed")
        self.assertEqual(self.student.courses, {})

    def test_leave_course_if_course_not_exists(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("B")
        expected = "Cannot remove course. Course not found."
        self.assertEqual(str(ex.exception), expected)
