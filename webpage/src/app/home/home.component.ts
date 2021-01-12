import { Component, OnInit } from '@angular/core';

import { Observable } from 'rxjs';
import { Woolball } from '@app/_models/woolball';
import { ActivatedRoute } from '@angular/router';
import { HomeService } from './home.service';
import { switchMap } from 'rxjs/operators';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  woolballs$: any; //Observable<Woolball[]>;
  selectedId: string

  constructor(
    private homeService: HomeService,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.homeService.getWoolballs()
      .subscribe(
        data => {
          this.woolballs$ = data.woolballs;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

}
