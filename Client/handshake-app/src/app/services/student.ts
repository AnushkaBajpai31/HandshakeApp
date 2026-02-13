import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { AppConstants } from '../app.constants';

@Injectable({
  providedIn: 'root',
})
export class Student {
  constructor(private http: HttpClient, private api_constants: AppConstants) {}

  getStudentData() {
    return this.http.get(this.api_constants.STUDENT_DATA_URL);
  }
}
