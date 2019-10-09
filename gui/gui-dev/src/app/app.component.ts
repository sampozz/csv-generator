import { Component } from '@angular/core';
import { FileService } from './services/file.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  
  configs = {}

  constructor(
    private file: FileService
  ) {
    file.getConfigs().then(data => {
      this.configs = data;
      console.log(this.configs)
    });
  }

}
