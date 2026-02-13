import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { Student as StudentService } from '../../services/student';
import { ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-student',
  imports: [CommonModule],
  templateUrl: './student.html',
  styleUrl: './student.css',
})
export class Student {

  constructor(private studentService: StudentService, private changeDetectorRef: ChangeDetectorRef) {}
  students: any = [];

  ngOnInit() 
  {
    this.getStudentData();
  }

  getStudentData() 
  {
    this.studentService.getStudentData().subscribe({
      next: (data) => {
        this.students = data;
        this.changeDetectorRef.detectChanges();
      },
      error: (err) => console.error(err)
    });
  }

}
