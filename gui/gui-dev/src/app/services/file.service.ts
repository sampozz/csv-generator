import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class FileService {

  configs = {};

  constructor(
    private http: HttpClient
  ) { }

  getConfigs() { 
    return this.http.get('assets/configs.json').toPromise();
  }
}
