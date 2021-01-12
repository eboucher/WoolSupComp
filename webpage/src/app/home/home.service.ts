import { Injectable } from '@angular/core';

import { Observable, of } from 'rxjs';
import { map } from 'rxjs/operators';

import { Woolball } from '@app/_models/woolball';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class HomeService {

  woolball: any;

  constructor(private http: HttpClient) { }

  private _url : string = 'http://127.0.0.1:5000/woolballs'

  getWoolballByID(id: string) : any {
    return this.http.get<Woolball[]>(this._url+id)
      .pipe(map(resp => {
        this.woolball = resp;
        return resp;
      }));
  }

  getWoolballs(): any { //Observable<Woolball[]> {
    return this.http.get<Woolball[]>(this._url);
  }

  getWoolball(id: number | string): Observable<Woolball> {
    return this.getWoolballs().pipe(
      map((woolballs: Woolball[]) => woolballs.find(woolball => woolball.id === id))
    );
  }
}